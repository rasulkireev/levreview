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

  close() {
    this.menuTarget.classList.add("hidden");
    this.buttonTarget.setAttribute("aria-expanded", "false");
  }

  hideOnOutside(event) {
    if (!this.element.contains(event.target)) {
      this.close();
    }
  }
}
