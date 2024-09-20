const express = require('express');
const app = express();

const User = require('./models/user');  // mmda de Lalo
const Place = require('./models/place');  // mmdda de Lalo

app.use(express.json());

app.post('/recommendations', async (req, res) => {
  const { userId, currentLocation } = req.body;

  const user = await User.findById(userId);
  const preferences = user.preferences;

  const nearbyPlaces = await Place.find({
    location: {
      $near: {
        $geometry: { type: "Point", coordinates: [currentLocation.lng, currentLocation.lat] },
        $maxDistance: 1000  
      }
    },
    type: { $in: preferences }
  });

  res.json(nearbyPlaces);
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
