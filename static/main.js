// Wait for doc to load before executing any functions

var dataPicker;

$(function () {
    console.log("hello")

    // $( function() {
    //     $( "#datepicker" ).datepicker();
    //   } );


    datePicker = $('#datetimepicker12').datetimepicker({
        inline: true,
        sideBySide: true
    });
});


function testTime(){
    console.log("test time");
    console.log(datePicker.data("date"))
    // $('#datetimepicker').data("DateTimePicker").FUNCTION()
}

{/* <script type="text/javascript">
                // $(function () {
                //     $('#datetimepicker12').datetimepicker({
                //         inline: true,
                //         sideBySide: true
                //     });
                // });

                $(function () {
                    $('#datetimepicker12').datetimepicker({
                        inline: true,
                        sideBySide: true
                    });
                });
            </script> */}

