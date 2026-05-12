const TROY_OUNCE_GRAMS = 31.1035;
const PRICE_REFRESH_SECONDS = 60;
const goldOunce = document.getElementById("gold-ounce");
const goldGram = document.getElementById("gold-gram");
const silverOunce = document.getElementById("silver-ounce");
const silverGram = document.getElementById("silver-gram");
const priceStatus = document.getElementById("price-status");
const priceUpdated = document.getElementById("price-updated");
const priceCountdown = document.getElementById("price-countdown");
const priceError = document.getElementById("price-error");
const onlineUserList = document.getElementById("online-user-list");
let secondsUntilRefresh = PRICE_REFRESH_SECONDS;
let isOnlineCarouselPaused = true;

const usdFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  maximumFractionDigits: 2,
});

const gramFormatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  maximumFractionDigits: 4,
});

function setPriceStatus(text, type = "ready") {
  priceStatus.textContent = text;
  if (type === "ok") {
    priceStatus.style.background = "#dcfce7";
    priceStatus.style.color = "#15803d";
  } else if (type === "error") {
    priceStatus.style.background = "#fee2e2";
    priceStatus.style.color = "#991b1b";
  } else {
    priceStatus.style.background = "#e0f2fe";
    priceStatus.style.color = "#0369a1";
  }
}

function showPriceError(message = "") {
  priceError.textContent = message;
  priceError.style.display = message ? "block" : "none";
}

function updatePriceView(gold, silver) {
  goldOunce.classList.remove("loading");
  silverOunce.classList.remove("loading");
  goldOunce.textContent = usdFormatter.format(gold);
  silverOunce.textContent = usdFormatter.format(silver);
  goldGram.textContent = gramFormatter.format(gold / TROY_OUNCE_GRAMS);
  silverGram.textContent = gramFormatter.format(silver / TROY_OUNCE_GRAMS);
  priceUpdated.textContent = new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => {
    const entities = {
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    };
    return entities[char];
  });
}

function scrollOnlineUsers(direction = 1) {
  if (!onlineUserList) return;
  const firstUser = onlineUserList.querySelector(".user-item");
  const cardWidth = firstUser ? firstUser.offsetWidth + 12 : 272;
  const maxScroll = onlineUserList.scrollWidth - onlineUserList.clientWidth;

  if (maxScroll <= 0) return;

  const nextLeft = onlineUserList.scrollLeft + cardWidth * direction;
  const targetLeft =
    nextLeft > maxScroll ? 0 : nextLeft < 0 ? maxScroll : nextLeft;

  onlineUserList.scrollTo({
    left: targetLeft,
    behavior: "smooth",
  });
}

document.querySelectorAll("[data-online-scroll]").forEach((button) => {
  button.addEventListener("click", () => {
    scrollOnlineUsers(Number(button.dataset.onlineScroll));
  });
});

if (onlineUserList) {
  onlineUserList.addEventListener("mouseenter", () => {
    isOnlineCarouselPaused = true;
  });
  onlineUserList.addEventListener("mouseleave", () => {
    isOnlineCarouselPaused = false;
  });
}

async function fetchMetalPrices() {
  setPriceStatus("Updating", "loading");
  showPriceError();

  try {
    const response = await fetch("/api/price", {
      headers: { Accept: "application/json" },
      cache: "no-store",
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status} ${response.statusText}`);
    }

    const prices = await response.json();
    const gold = Number(prices.XAU);
    const silver = Number(prices.XAG);

    if (!Number.isFinite(gold) || !Number.isFinite(silver)) {
      throw new Error("Unexpected price response from /api/price");
    }

    updatePriceView(gold, silver);
    secondsUntilRefresh = PRICE_REFRESH_SECONDS;
    priceCountdown.textContent = `${secondsUntilRefresh}s`;
    setPriceStatus("Live", "ok");
  } catch (err) {
    setPriceStatus("Unavailable", "error");
    showPriceError(`Price feed unavailable: ${err.message}`);
  }
}

async function fetchLiveActivity() {
  const userList = onlineUserList;
  if (!userList) return;

  try {
    const response = await fetch("/api/online");
    if (!response.ok)
      throw new Error(`HTTP ${response.status} ${response.statusText}`);

    const users = await response.json();

    const countSpan = document.getElementById("live-count");
    if (countSpan) {
      const totalUsers = users ? users.length : 0;
      countSpan.textContent = `${totalUsers} online`;
    }

    if (!users || users.length === 0) {
      userList.innerHTML = `<div class="online-state">No active users right now</div>`;
      return;
    }

    userList.innerHTML = users
      .reverse()
      .slice(0, 12)
      .map((user) => {
        const city = user.city || "Unknown";
        const country = /^[A-Z]{2}$/i.test(user.country || "")
          ? user.country.toUpperCase()
          : "SO";
        const org = user.org || "API visitor";
        const initials = city
          .split(/\s+/)
          .filter(Boolean)
          .slice(0, 2)
          .map((part) => part[0])
          .join("")
          .padEnd(2, country[0] || "U")
          .slice(0, 2);

        return `
      <div class="user-item">
        <div class="user-avatar">${escapeHtml(initials)}</div>
        <div class="user-details">
          <span class="user-location">${escapeHtml(city)}</span>
          <span class="user-meta">
            <img src="https://flagsapi.com/${country}/flat/16.png" alt="">
            ${escapeHtml(country)}
          </span>
        </div>
      </div>
    `;
      })
      .join("");
  } catch (err) {
    console.error("Live Activity Error:", err);
    const countSpan = document.getElementById("live-count");
    if (countSpan) {
      countSpan.textContent = "Unavailable";
    }
    userList.innerHTML = `<div class="online-state">Activity feed unavailable: ${escapeHtml(err.message)}</div>`;
  }
}

// Wicitaan markasta 60 seconds
fetchLiveActivity();
setInterval(fetchLiveActivity, 60000);
// setInterval(() => {
//   if (!isOnlineCarouselPaused) {
//     scrollOnlineUsers(1);
//   }
// }, 4500);

fetchMetalPrices();
setInterval(fetchMetalPrices, PRICE_REFRESH_SECONDS * 1000);
setInterval(() => {
  secondsUntilRefresh = Math.max(secondsUntilRefresh - 1, 0);
  priceCountdown.textContent = `${secondsUntilRefresh}s`;
}, 1000);

// Heartbeat to keep user 'online'
setInterval(() => {
  fetch("/api/ping").catch((err) => console.error("Ping failed:", err));
}, 25000); // Ping every 25 seconds
