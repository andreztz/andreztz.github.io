# Como apagar a lista assistir mais tarde do youtube


1- Abra [your watch later playlist](https://www.youtube.com/playlist?list=WL&disable_polymer=true) no youtube.

2- Abra o console de desenvolvimento do seu navegador ( Ctrl+Shift+J para o chrome, Ctrl+Shift+K para o firefox )

3- Cole o seguinte script no console


```js {linenos=true}

// execute removeOne() every 30 milliseconds
var interval = setInterval(removeOne, 30) 

// the number of displayed videos in the last execution of removeOne()
var lastNumVideos = 0

function removeOne () {
  // number of videos displayed
  var numVideos = document.querySelectorAll('.pl-video-edit-remove').length
  if (numVideos === lastNumVideos) {
    return // skip removal if the previously removed video is still present
  }
  if (numVideos < 1) {
    try {
      // click load more if there are no displayed videos
      document.querySelector('.browse-items-load-more-button').click()
    } catch (err) {
      console.log('Load More button is missing. Refresh the page and restart the script to remove more videos.')
      // stop repeating removeOne()
      clearInterval(interval)
    }
  } else {
    // remove top most video
    document.querySelector('.pl-video-edit-remove').click() 
    lastNumVideos = numVideos
  }
}
```

4- Pressione a tecla Enter, e aguarde o script finalizar.

5- Atualize a página (F5 para atualizar), se ainda existir videos na playlist volte ao passo 3, caso contrário seja feliz.


Se você precisar parar o script feche ou atualize a aba do seu navegador.

