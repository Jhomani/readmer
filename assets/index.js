let pages;

const main = document.getElementById('content');

window.onpopstate = (ev) => {
  console.log('back', ev)
}

window.onunload = () => window.location.href = '/index.html'; 

const changeRoute = (target) => {
  main.innerHTML = pages[target]; 
  window.history.pushState(pages[target], target, `/${target}`);
}

const natigationItems = document.querySelectorAll('.sidebar-content_items > li');

const handleNavigate = (target) => {
  console.log(target);
  changeRoute(target);
}

natigationItems.forEach(ele => {
  ele.onclick = handleNavigate.bind({}, ele.getAttribute('name'));
})

fetch('/pages.json')
  .then(encoded => encoded.json())
  .then(datas =>{
    pages = datas;
    changeRoute('index');
  });