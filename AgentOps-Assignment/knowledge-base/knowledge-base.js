const axios = require('axios');

async function getLocationInfo(city) {
  const res = await axios.get(`http://your-api.com/api/location?city=${city}`);
  return res.data;
}

async function getMenuInfo(type) {
  const res = await axios.get(`http://your-api.com/api/menu?type=${type}`);
  return res.data;
}

module.exports = { getLocationInfo, getMenuInfo };
