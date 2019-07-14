title: Como apagar a lista assistir mais tarde do youtube
slug: como-apagar-a-lista-assitir-mais-tarde-do-youtube
date: 2019-07-14
category: web
tags: web, internet, youtube
Authors: André P. Santos
Summary: Como apagar a lista assistir mais tarde do youtube


1- Abra [your watch later playlist](https://www.youtube.com/playlist?list=WL&disable_polymer=true) no youtube.

2- Abra o console de desenvolvimento do seu navegador ( Ctrl+Shift+J para o chrome, Ctrl+Shift+K para o firefox )

3- Cole o seguinte script no console


``` javascript
var interval = setInterval(removeOne, 30) // execute removeOne() every 30 milliseconds

var lastNumVideos = 0 // the number of displayed videos in the last execution of removeOne()

function removeOne () {
  var numVideos = document.querySelectorAll('.pl-video-edit-remove').length // number of videos displayed
  if (numVideos === lastNumVideos) {
    return // skip removal if the previously removed video is still present
  }
  if (numVideos < 1) {
    try {
      document.querySelector('.browse-items-load-more-button').click() // click load more if there are no displayed videos
    } catch (err) {
      console.log('Load More button is missing. Refresh the page and restart the script to remove more videos.')
      clearInterval(interval) // stop repeating removeOne()
    }
  } else {
    document.querySelector('.pl-video-edit-remove').click() // remove top most video
    lastNumVideos = numVideos
  }
}
```

4- Pressione a tecla Enter, e aguarde o script finalizar.

5- Atualize a página (F5 para atualizar), se ainda existir videos na playlist volte ao passo 3, caso contrário seja feliz.


Se você precisar parar o script feche ou atualize a aba do seu navegador.
