navigator.geolocation.getCurrentPosition(position => {
    const {latitude, longitude} = position.coords;
    
    map.innerHTML = `<iframe width="" height="300" src="https://maps.google.com/maps?q=${latitude},${longitude}&amp;output=embed"></iframe>`;
});
 