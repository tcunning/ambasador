var overviewApp = angular.module('overviewApp', []);

// Allow Django to use {{ xyz }} variables and a
// Allow angular to use {[{ xyz }]} variables 
overviewApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
 
// MARK 2

overviewApp.controller('ReferralListController', ['$scope', '$window', '$http',function($scope, $window, $http) {
    var referralList = this;
    
    referralList.referrals = $window.initialReferrals;
    //
    //referralList.initialReferralRemaining = function() {
    //   return referralList.initialReferral.count;
    //};    
    
    //referralList.todos = [
    //    {text:'learn angular', done:true},
    //    {text:'build an angular app', done:false}];

    referralList.addReferral = function() {
        var referral = {name:referralList.referralText, count:0};
        
        $http.post("/referral/?format=json", referral)
        .success(function (data, status, headers, config) {
            referralList.referrals.push(referral);
            referralList.referralText = '';
        })
        .error(function (data, status, header, config) {
            alert("Unable to update data!");
        });       
    };

    referralList.removeReferral = function(referral) {
        var referralIndex = referralList.referrals.indexOf(referral)
        referralList.referrals.splice(referralIndex,1)
    };

    referralList.refresh = function() {
        $http.get('/referral/?format=json')
        .success(function (data, status, headers, config) {
            referralList.referrals = data;
        })
        .error(function (data, status, header, config) {
            alert("Unable to refresh data!");
        });
    };
    
    //referralList.remaining = function() {    
    //   var count = 0;
    //   angular.forEach(referralList.todos, function(todo) {
    //      count += todo.done ? 0 : 1;
    //   });
    //   return count;
    //};

    //referralList.archive = function() {
    //   var oldTodos = referralList.todos;
    //   referralList.todos = [];
    //   angular.forEach(oldTodos, function(todo) {
    //      if (!todo.done) referralList.todos.push(todo);
    //   });
    //};
}]);

