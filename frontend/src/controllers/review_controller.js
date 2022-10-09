import { Controller } from "@hotwired/stimulus";
import {enter} from 'el-transition';

export default class extends Controller {
  static targets = [ "form", "rating" ];

  fillStars(event) {
    const clickedStarNumber = parseInt(event.currentTarget.id);
      this.eraseAllStars();
      for (let i = clickedStarNumber; i > 0; i--) {
        document.getElementById(`${i}`).setAttribute("fill", "currentColor");
      }
      this.next(clickedStarNumber);
      this.ratingTarget.setAttribute("value", clickedStarNumber);
  }

  eraseAllStars() {
    for (let i = 5; i > 0; i--) {
      document.getElementById(`${i}`).setAttribute("fill", "none");
    }
  }

  next(clickedStarNumber) {
    const minRating = parseInt(this.formTarget.getAttribute("value"));

    if (clickedStarNumber < minRating) {
      enter(this.formTarget);
    }
  }
}