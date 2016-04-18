/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var PRODUCT_APP={
    /*Returning jQuery Promise For a AJAX call with Product type*/
    getProductDetails : function(type){
          var ajaxRequest=$.ajax("ProductServlet?type="+type);
          return ajaxRequest.promise();
    },
    /*Handler For AJAX response*/
    handleCallback : function(type){
        var promise = PRODUCT_APP.getProductDetails(type);
        promise.done(function(data){
            PRODUCT_APP.doProductRendering(data);
        });
    },
    /*jQuery Template building with JSON data  from Server*/
    doProductRendering: function(data){
        var productContainer =$('.ts-product-container'),
            aProductTemplate = $('#aProductTemplate').tmpl( data )
            /*,
            promiseOldPro = $(productContainer).find('.panel').fadeOut().promise(); 
            $.when(promiseOldPro).then(function(){
            */
            productContainer.html(aProductTemplate);
        //});
    },
    /*Event Listener per il  tag h3 con id h3_1*/
    init_h3_1_Click:function(){
        $("").on('click','li',function(e){
            e.preventDefault();
            var li = e.currentTarget,
                type= $(li).attr('data-category');
            $(li).siblings('li').removeClass('active');
            $(li).addClass('active');
            PRODUCT_APP.handleCallback(type);
        });
    }
};

$(document).ready(function(){
    /*Initial Load Call Books */
   /* PRODUCT_APP.handleCallback('book'); */
    /*Initialize Click Of Menu Item*/
   PRODUCT_APP.initCategoryClick();
});


