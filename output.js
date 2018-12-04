const fs = require('fs');
fs.writeFileSync("cache/eu-schedule-rooms.json", JSON.stringify(opScheduleRooms))

fs.writeFileSync("cache/eu-speakers.json", JSON.stringify(opSpeakers))
fs.writeFileSync("cache/eu-organisers.json", JSON.stringify(opOrganisers))
