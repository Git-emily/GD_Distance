$(function(){
   $("#get_coordinate").click(function(){
    var city_A = $('#city_A').val();
    var city_B = $('#city_B').val();
    var url = 'https://restapi.amap.com/v3/geocode/geo';
    $.get(
        url,
        {
            key: "5c5cf68cefc1682dcbfdf84a3a7d88c2",
            address: city_A + '|' + city_B,
            batch:true
        }, function(data){
            $("#init_result1").html(data.geocodes[0].location) 
            $("#init_result2").html(data.geocodes[1].location)
        });
   });

   $("#cal_distance").click(function(){
       var st = $("#init_result1").html();
       var ed = $("#init_result2").html();
       var url2 = "https://restapi.amap.com/v3/distance";
       $.get(
           url2,
           {
            key:"33f11904550840bc85c725842a57bd04",   
            origins:st,
            destination:ed,
           },function(data){
               distance_meter = data.results[0].distance;
               $("#distance").html((distance_meter/1000).toFixed(1));
           });

   });

   $("#clear").click(function(){
       $("#city_A").val('');
       $("#city_B").val('');
       $("#init_result1").html('');
       $("#init_result2").html('');
       $("#distance").html('');
   });
})
