// Wait for doc to load before executing any functions

var dataPicker;

$(function () {


    var currentPage = window.location.href;
    
    // Initialize datetimepicker if on create page, otherwise
    // Update Projects layout if on the projects page
    // indexOf returns -1 if substring is not found
    if (currentPage.indexOf('/createProject') > -1) {
        console.log("running date time picker")
        
        datePicker = $('#datetimepicker12').datetimepicker({
            inline: true,
            sideBySide: true
        });
        console.log(datePicker.data("date"))
    }
    else if (currentPage.indexOf('/projects') > -1 ){
    
        updateProjectsLayout();
    }
    
    
});

// testTime no longer defined, was using it on button click in createProject.html


function updateProjectsLayout(){

    // get json data from python
    console.log("updating projects layout")

    $.getJSON("/updateProjects", function(data, textStatus, jqXHR) {
        console.log("this is the data from updateProjects python", data);



    });

}