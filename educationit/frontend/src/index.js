console.log('test')
import axios from 'axios'

let htmlItems = document.getElementById('items')
axios.get('/api/courses/')
  .then(function (response) {
    if (response.status === 200) drawItems(response.data)
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });
  function drawItems(items) {
    items.forEach((item) => {
        console.log(item)
        let newElement = document.createElement('div')
        newElement.id = item.id
        newElement.className = "item"
        newElement.innerHTML = `${item.id}) ${item.name} - ${item.description}`
        htmlItems.appendChild(newElement)
    })
}