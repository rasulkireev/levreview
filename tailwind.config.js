module.exports = {
  content: [
    './templates/**/*.html',
    './foxreview/utils.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
