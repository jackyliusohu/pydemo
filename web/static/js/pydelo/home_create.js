$(document).ready(function() {
    $("#submit").click(function(e){
        create_home(
            {"name": $("#name").val(), "ssh_host": $("#ssh_host").val(), "ssh_port": $("#ssh_port").val(), "ssh_user": $("#ssh_user").val(), "ssh_method": $("#ssh_method").val(), "ssh_pass": $("#ssh_pass").val()},
            function(data1){
            console.log(data);
            alert(data);
                check_return(data);
                window.location.assign('/homes');
        });
    });
})
