let pages;

const main = document.getElementById('content');

window.onpopstate = (ev) => {
  main.innerHTML = ev.state;
}

const changeRoute = (target) => {
  main.innerHTML = pages[target];

  window.history.pushState(pages[target], target, `/?page=${target}`);

  const codeBox = main.querySelector("code.language-json")
  let jsonTxt = codeBox?.innerHTML || "";

  if (jsonTxt)
    codeBox.innerHTML = prettyJson(jsonTxt);
}

const prettyJson = (jsonTxt) => {
  let keySeparator = false;
  let readyToClose = false;

  for (let i = 0; i < jsonTxt.length; i++) {
    if ((jsonTxt[i] === '{' || jsonTxt[i] === ',') && !readyToClose)
      keySeparator = true;

    if (keySeparator && !readyToClose && jsonTxt[i] === '"') {
      let startTag = "<span class=\"green-2\">";

      jsonTxt = jsonTxt.slice(0, i) + startTag + jsonTxt.slice(i);
      i += startTag.length;

      readyToClose = true;
    }

    if (readyToClose && jsonTxt[i] === '"' && jsonTxt[i + 1] === ":") {
      let endTag = "</span>";

      jsonTxt = jsonTxt.slice(0, i + 1) + endTag + jsonTxt.slice(i + 1);
      i += endTag.length;

      readyToClose = false;
      keySeparator = false
    }
  }

  return jsonTxt;
}

const appendToSideBar = (itemsList = []) => {
  const sidebar = document.querySelector('.sidebar-content_items');

  itemsList.forEach(item => {

    let position = "beforeend";
    if (item === 'main') position = "afterbegin"

    sidebar.insertAdjacentHTML(position, `
      <li name='${item}'>
        <a>
          <span class="sidebar_icon">&#128466;</span>
          <span role="text">${item}</span>
        </a>
      </li>
    `);
  });

  const natigationItems = sidebar.querySelectorAll('li');

  natigationItems.forEach(ele => {
    ele.onclick = changeRoute.bind({}, ele.getAttribute('name'));
  })
}

fetch('/pages.json')
  .then(encoded => encoded.json())
  .then(datas => {
    pages = datas;

    appendToSideBar(Object.keys(pages))

    changeRoute('main');
  });