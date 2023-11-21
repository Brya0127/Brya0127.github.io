scrollTrigger('.loader, {
  cb: function(el) {
    el.innerText = 'Loading...'
    loadContent()
  }
})

function scrollTrigger(selector) {
  // can us same class/selector
  lets els = document.querySelectorAll(selector)
  // array
  els = Array.from(els)
  els.forEach(el => {
    addObserver(el)
  })
}
// scrollTrigger('.ease-assets')
scrollTrigger('.scroll-reveal')

function addObserver(el){
  let observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('active')
      observer.unobserve(entry.target)
    }
    
    })
  })
  // adds observer to element
  observer.observe(el)

}

scrollTrigger ('.scroll-reveal')

// adds active class once more of element is revealed

function scrollTrigger(selector, options = {}) {
  lets els = document.querySelectorAll(selector)
  els = Array.from(els)
  els.forEach(el => {
    addObserver(el, options)
  })
}

// options

function addObserver(el, options) {
  let observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('active')
        observer.unobserve(entry.target)
      }
    })
  }, options)
  observer.observe(el)
}

// example again

scrollTrigger('.scroll-reaveal', {
  rootMargin: '-200px'
})

function scrollTrigger(selector, options = {}) {
  let els = document.querySelectorAll(selector)
  els = Array.from(els)
  els.forEach(el => {
    addObserver(el, options)
  })
}
function addObserver(el, options) {
  let observer = new IntersectionObserver((entries,observer) => {
    entries.forEach(entry => {
      if(entry.isIntersecting){
        if(options.cb) {
          options.cb(el)
        } else {
          entry.target.classList.add('active')
        }
        observer.unobserve(entry.target)
      }
    })
  }, options)
  observer.observe(el)
}

// example
scrollTrigger('.loader', {
  rootMargin: '-200px',
  cb:function(el){
    el.innerText = 'Loading...'
    // finished
    setTimeout(() => {
      el.innerText = 'Done!'
    }, 1000)
  }
})

