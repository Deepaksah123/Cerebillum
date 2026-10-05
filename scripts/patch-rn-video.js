const fs = require('fs');
const path = require('path');

const file = path.join(
  __dirname, '..', 'node_modules', 'react-native-video', 'android', 'src',
  'main', 'java', 'com', 'brentvatne', 'common', 'react', 'VideoEventEmitter.kt'
);

if (!fs.existsSync(file)) {
  console.log('react-native-video source not present; nothing to patch.');
  process.exit(0);
}

let source = fs.readFileSync(file, 'utf8');

if (source.includes('dispatcher.dispatchEvent(VideoEvent(surfaceId, viewId, eventName, eventData))')) {
  console.log('react-native-video compatibility patch already applied.');
  process.exit(0);
}

const start = source.indexOf('private class EventBuilder(');
const end = source.indexOf('    private fun audioTracksToArray', start);

if (start < 0 || end < 0) {
  throw new Error('react-native-video EventBuilder boundaries not found; refusing unsafe patch.');
}

const replacement = String.raw`private class EventBuilder(private val surfaceId: Int, private val viewId: Int, private val dispatcher: EventDispatcher) {
        fun dispatch(event: EventTypes, paramsSetter: (WritableMap.() -> Unit)? = null) {
            val eventName = "top\${event.eventName.removePrefix("on")}"
            val eventData = Arguments.createMap().apply(paramsSetter ?: {})
            dispatcher.dispatchEvent(VideoEvent(surfaceId, viewId, eventName, eventData))
        }
    }

`;

source = source.slice(0, start) + replacement + source.slice(end);
fs.writeFileSync(file, source);
console.log('Applied deterministic react-native-video VideoEvent compatibility patch for RN 0.81.');
