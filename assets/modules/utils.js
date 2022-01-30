const main = document.getElementById('content');

window.onpopstate = (ev) => {
  console.log('back', ev)
}

export const changeRoute = (target) => {
  main.innerHTML = datas[target]; 
  window.history.pushState(datas[target], target, target);
}