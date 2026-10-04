const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'node_modules', 'react-native-video', 'android', 'src', 'main', 'java', 'com', 'brentvatne', 'common', 'react', 'VideoEventEmitter.kt');

if (!fs.existsSync(file)) { console.log('react-native-video source not present; nothing to patch.'); process.exit(0); }

let source = fs.readFileSync(file, 'utf8');
const oldText = 'dispatcher.dispatchEvent(VideoEvent(surfaceId, viewId, eventName, eventData))';
const newText = 'dispatcher.dispatchEvent(object : Event<Event<*>>(surfaceId, viewId) {\n          override fun getEventName() = eventName\n          override fun getEventData() = eventData\n        })';

if (source.includes(newText)) { console.log('react-native-video compatibility patch already applied.'); process.exit(0); }
if (!source.includes(oldText)) throw new Error('react-native-video VideoEventEmitter.kt did not match expected source; refusing unsafe patch.');
source = source.replace(oldText, newText);
fs.writeFileSync(file, source);
console.log('Applied deterministic react-native-video Event<Event<*>> compatibility patch.');
