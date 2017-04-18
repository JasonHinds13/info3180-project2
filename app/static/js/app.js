/* global angular */

var app = angular.module("imgApp", []);

app.controller("imgCtrl", function($scope, $http){
    $http.get('/api/thumbnails').then(function(response){
        $scope.images = response.data["thumbnails"];
    });
});