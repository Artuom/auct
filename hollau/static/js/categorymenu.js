console.log('at the start');
function DropDown(el) {
    this.dd = el;
    this.initEvents();
    console.log('In func');
}
DropDown.prototype = {
    initEvents : function() {
        var obj = this;
        obj.dd.on('click', function(event){
            $(this).toggleClass('active');
            event.stopPropagation();
            console.log('Ok');
        });
    }
}