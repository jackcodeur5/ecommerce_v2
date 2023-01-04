

var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click',function(){
         var productId = this.dataset.product
         var action = this.dataset.action
         addCartItem(productId, action)
         console.log('USER:', user)
         if(user == 'AnonymousUser'){
            addCartItem(productId, action)
         }else{
            updateUserOrder(productId, action)
         } 
     })
} 
/*
$(document).on('click', '.update-cart', function(){
    var productId = this.dataset.product
  var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('User:', user)
    if(user === 'AnonymousUser'){
        addCartItem(productId, action)
    }else{
        updateUserOrder(productId, action)
    }

}) */

function addCartItem(productId, action){
    console.log('User is not Autenticate!')
    console.log('User:', user)
    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'qte_produit': 1}
        }else{
            cart[productId]['qte_produit'] += 1

        }
    }

    if(action == 'remove'){
       cart[productId]['qte_produit'] -= 1
       if(cart[productId]['qte_produit'] <= 0){
           console.log("Supprimer produit")
           delete cart[productId]

       }
    }
    
   
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    // location.reload()
    // window.reload()
   if(window.location.href == "http://127.0.0.1:8000/panier/"){
    location.reload() 
    window.reload()
 
   }else{
    window.location.href = "http://127.0.0.1:8000/panier/"
    window.reload()
    // alert(window.location.href);
   }
    


    /*var path = location.pathname
        console.log(path)
        if(path == '/panier/'){
            location.reload()
        }else{
            window.location.href = "panier/"
        }*/
     
}
/*
function updateUserOrder(productId, action){
    
    $.ajax({
        url : '/update_items/',
        data: {'productId': productId, 'action': action},
        dataType:'json',
        success: function(){
            location.reload()
            
        }
    })
} */

function updateUserOrder(productId, action){
    console.log('User  logged is sending data...')

    var url = '/update_items/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data) 
        location.reload()
    })
} 

var catbtns = document.getElementsByClassName("categorie");
for(var i=0; i<catbtns.length; i++){
    catbtns[i].addEventListener('click', function (){

        var categorie_id = this.dataset.categorie;
        console.log("Id de la catégorie:", categorie_id);
        var url = '/product_by_categorie';

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'categorie_id': categorie_id})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        produits = JSON.parse(data['json_data'])
        // produits_id = JSON.parse(data['json_id'])
        // console.log(produits)
        var div = document.getElementById('catProduits')
         for(var i=0; i<produits.length; i++ ){
            console.log(produits[i])
           var divData = 
            '<div class="card shadow  col-xl-4 ">'+
            '<div class="text-center"><a href="page_produit/'+produits[i]['pk']+ '"><img class="img-fluid px-3 px-sm-4 mt-3 mb-4" style="width: 25rem; height: 12rem;" src="/medias/'+produits[i]['fields']['image']+'" ></a></div>'+
            '</div>';
            div.insertAdjacentHTML('beforeend', divData);
         }


    })
    })
}

/*
$(document).on('click', '.update-cart', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('User:', user)

})
 

function updateUserOrder(productId, action){
		$.ajax({
			type:"POST",
			url:"{% url 'update_items' %}",
            data:{
                productId:productId,
                action:action,
                csrfMiddlewaretoken:csrftoken,
            },
			success:function(response){
				console.log(response);
			},
			error:function(response){
				//alert('error!');
			}
		})

} */