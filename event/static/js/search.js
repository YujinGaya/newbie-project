angular.module('search', [])
    .controller('searchController', function SearchController($scope, $http) {


        $http.get('/events')
            .then(function(data){
                $scope.events = JSON.parse(data.data);
                for(var i = 0; i < $scope.events.length; i++){
                    time = moment($scope.events[i].fields.time);
                    if (time.isBefore(moment().add(10, 'days'))) {
                        $scope.events[i].fields.parsed_time = time.fromNow() + ' ' + time.format('kk:mm');
                    } else {
                        $scope.events[i].fields.parsed_time = time.format('M월 D시 kk:mm');
                    }

                }
        });
});
