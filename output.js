const fs = require('fs');
fs.writeFileSync("eu-schedule-rooms.json", JSON.stringify(opScheduleRooms))

fs.writeFileSync("eu-speakers.json", JSON.stringify(opSpeakers))
fs.writeFileSync("eu-organisers.json", JSON.stringify(opOrganisers))
