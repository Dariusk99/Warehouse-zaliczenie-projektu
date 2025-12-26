class Modal {
    constructor() {
        this.createModal();
    }

    createModal() {
        this.modalElement = document.createElement("div");
        this.modalElement.classList.add("modal");
        this.modalElement.style.display = "none";

        const modalContent = document.createElement("div");
        modalContent.classList.add("modal-content");

        const closeButton = document.createElement("span");
        closeButton.classList.add("close");
        closeButton.innerHTML = "&times;";
        closeButton.addEventListener("click", () => {
            this.close();
        });

        modalContent.appendChild(closeButton);
        this.modalElement.appendChild(modalContent);
    }

    open(htmlContent) {
        const modalContent = this.modalElement.querySelector(".modal-content");
        modalContent.insertAdjacentHTML("beforeend", htmlContent);
        this.modalElement.style.display = "block";
    }

    close() {
        if (this.modalElement) {
            this.modalElement.remove();
            this.modalElement = null;
        }
    }
}
