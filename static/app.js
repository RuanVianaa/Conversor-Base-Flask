(() => {
  const modal = document.getElementById("result-modal");
  if (!modal) return;

  const closeModal = () => {
    modal.classList.add("closing");
    window.setTimeout(() => modal.remove(), 120);
  };

  document.getElementById("close-modal")?.addEventListener("click", closeModal);
  document.getElementById("done-modal")?.addEventListener("click", closeModal);
  modal.addEventListener("click", (event) => {
    if (event.target === modal) closeModal();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeModal();
  });

  document.getElementById("copy-result")?.addEventListener("click", async (event) => {
    const value = document.getElementById("result-value")?.textContent?.trim();
    if (!value) return;
    try {
      await navigator.clipboard.writeText(value);
      event.currentTarget.textContent = "Copiado!";
    } catch {
      event.currentTarget.textContent = "Não foi possível copiar";
    }
  });
})();
