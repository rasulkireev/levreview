import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
    static targets = [ "minRating" ];

    connect() {
      document.querySelector('#minRating').selectedIndex = this.minRatingTarget.value - 1;
    }
}
