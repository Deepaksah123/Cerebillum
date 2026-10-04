const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, '..', 'node_modules', 'react-native-video', 'android', 'src', 'main', 'java', 'com', 'brentvatne', 'common', 'react', 'VideoEventEmitter.kt');
if (!fs.existsSync(file)) { console.log('react-native-video source not present; nothing to patch.'); process.exit(0); }
let source = fs.readFileSync(file, 'utf8');
if (source.includes('dispatcher.dispatchEvent(object : Event<Event<*>>')) { console.log('react-native-video compatibility patch already applied.'); process.exit(0); }
const start = source.indexOf('private class EventBuilder(');
const end = source.indexOf('    private fun audioTracksToArray', start);
if (start < 0 || end < 0) throw new Error('react-native-video EventBuilder boundaries not found; refusing unsafe patch.');
const replacement = `private class EventBuilder(private val surfaceId: Int, private val viewId: Int, private val dispatcher: EventDispatcher) {
        fun dispatch(event: EventTypes, paramsSetter: (WritableMap.() -> Unit)? = null) =
            dispatcher.dispatchEvent(object : Event<Event<*>>(surfaceId, viewId) {
                override fun getEventName() = "top${event.eventName.removePrefix("on")}"
                override fun getEventData() = Arguments.createMap().apply(paramsSetter ?: {})
            })
    }

`;
source = source.slice(0, start) + replacement + source.slice(end);
fs.writeFileSync(file, source);
console.log('Applied deterministic react-native-video Event<Event<*>> compatibility patch.');
