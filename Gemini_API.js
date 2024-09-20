async function getAIRecommendations(userData) {
    const response = await fetch('https://gemini.api/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
  
    const data = await response.json();
    return data.recommendations;
  }
  
  app.post('/recommendations', async (req, res) => {
    const { userId, currentLocation } = req.body;
    const user = await User.findById(userId);
    const preferences = user.preferences;
  
    // Buscar lugares cercanos
    const nearbyPlaces = await Place.find({
      location: {
        $near: {
          $geometry: { type: "Point", coordinates: [currentLocation.lng, currentLocation.lat] },
          $maxDistance: 1000
        }
      },
      type: { $in: preferences }
    });
  
    const recommendations = await getAIRecommendations({
      userId,
      preferences,
      nearbyPlaces
    });
  
    res.json(recommendations);
  });
  