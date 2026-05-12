async function copyText(value) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(value);
    return;
  }

  const textarea = document.createElement("textarea");
  textarea.value = value;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.left = "-9999px";
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  textarea.remove();
}

document.querySelectorAll(".endpoint-url").forEach((endpoint) => {
  const button = endpoint.querySelector(".copy-btn");
  if (!button) return;

  button.addEventListener("click", async () => {
    const value = endpoint.dataset.copyUrl || endpoint.textContent.trim();
    const previousLabel = button.getAttribute("aria-label") || "Copy URL";

    try {
      await copyText(value);
      button.classList.add("copied");
      button.setAttribute("aria-label", "Copied");

      window.setTimeout(() => {
        button.classList.remove("copied");
        button.setAttribute("aria-label", previousLabel);
      }, 1600);
    } catch (error) {
      button.setAttribute("aria-label", "Copy failed");
      window.setTimeout(() => {
        button.setAttribute("aria-label", previousLabel);
      }, 1600);
    }
  });
});

