import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
static targets = [ "input", "button" ];

  connect() {
    console.log("ready");
    this.inputTarget.setAttribute("size", this.inputTarget.value.length);
  }

  copy() {
    navigator.clipboard.writeText(this.inputTarget.value);
    this.buttonTarget.classList.replace("bg-green-600", "bg-blue-600");
    this.buttonTarget.textContent = "Copied";
  }
}