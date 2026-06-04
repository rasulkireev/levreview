import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
  static targets = ["button", "menu"];

  connect() {
    this.close();
  }

  toggle(event) {
    event.stopPropagation();
    if (this.menuTarget.classList.contains("hidden")) {
      this.open();
    } else {
      this.close();
    }
  }

  open() {
    this.menuTarget.classList.remove("hidden");
    this.buttonTarget.setAttribute("aria-expanded", "true");
  }

  close(event) {
    this.menuTarget.classList.add("hidden");
    this.buttonTarget.setAttribute("aria-expanded", "false");

    if (event) {
      this.buttonTarget.focus({ preventScroll: true });
    }
  }

  closeOnEscape(event) {
    if (event.key === "Escape" && !this.menuTarget.classList.contains("hidden")) {
      this.close(event);
    }
  }

  hideOnOutside(event) {
    if (!this.element.contains(event.target)) {
      this.close();
    }
  }
}
