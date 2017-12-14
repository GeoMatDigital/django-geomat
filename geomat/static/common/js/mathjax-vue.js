window.onload = function () {
  let field = document.getElementById('id_chemical_formula')
  new Vue({
    el: '#editor',
    data: {
      input: '',
      output: ''
    },
    created: function () {
      this.input = field.value
    },
    watch: {
      input: _.debounce(function(e) {
        this.output = '\\(' + this.input + '\\)'
        this.$nextTick(function() {
          MathJax.Hub.Queue(["Typeset", MathJax.Hub, "editor-output"])
        })
      }, 300)
    }
  })
}
