import { useState } from "react";
import { useNavigate } from "react-router-dom";
import MapSelector from "../components/MapSelector";

export default function Predict(){

const navigate = useNavigate();

const [location,setLocation] = useState(null);

const [manualWeather,setManualWeather] = useState({
temperature:"",
humidity:"",
wind:""
});

const [form,setForm] = useState({
fire_count:"",
avg_frp:"",
max_frp:"",
night_ratio:"",
confidence:"",
trend:""
});

function update(e){
setForm({
...form,
[e.target.name]:e.target.value
});
}

function updateWeather(e){
setManualWeather({
...manualWeather,
[e.target.name]:e.target.value
});
}

function setExample(data){
setForm(data);
}

function runPrediction(e){

e.preventDefault();

let weather;

if(manualWeather.temperature){
weather={
temperature:Number(manualWeather.temperature),
humidity:Number(manualWeather.humidity),
wind:Number(manualWeather.wind)
};
}else{
if(!location){
alert("Select map location OR enter manual weather");
return;
}
weather=location;
}

let type1="Low";

if(Number(form.fire_count)>80) type1="High";
else if(Number(form.fire_count)>30) type1="Medium";

let type2="Low";

if(weather.temperature>35) type2="High";
else if(weather.temperature>28) type2="Medium";

let final="Low";

if(type1==="High" || type2==="High") final="High";
else if(type1==="Medium" || type2==="Medium") final="Medium";

const result={
type1,
type2,
final
};

localStorage.setItem("prediction",JSON.stringify(result));

navigate("/");
}

return(

<div className="max-w-6xl mx-auto space-y-8 text-white">

<h1 className="text-4xl font-bold text-yellow-400">
🔥 Wildfire Prediction
</h1>

{/* MAP */}

<div className="bg-slate-900/80 backdrop-blur-md p-4 rounded-xl shadow-xl border border-white/10">
<h3 className="mb-3 text-yellow-400">📍 Select Location</h3>

<div className="rounded-xl overflow-hidden">
<MapSelector setLocation={setLocation}/>
</div>

{location && (
<div className="mt-4 text-sm text-gray-300">
Lat: {location.lat.toFixed(3)} | Lon: {location.lng.toFixed(3)} <br/>
Temp: {location.temperature}°C | Humidity: {location.humidity}% | Wind: {location.wind} km/h
</div>
)}

</div>

{/* WEATHER INPUT */}

<div className="bg-slate-900/80 backdrop-blur-md p-4 rounded-xl shadow-xl border border-white/10">

<h3 className="text-yellow-400 mb-3">
🌦 Manual Weather (Optional)
</h3>

<div className="grid md:grid-cols-3 gap-4">

<input name="temperature" placeholder="Temperature °C" value={manualWeather.temperature} onChange={updateWeather}
className="p-3 rounded-lg bg-slate-800 border border-white/10 focus:ring-2 focus:ring-yellow-400 outline-none"/>

<input name="humidity" placeholder="Humidity %" value={manualWeather.humidity} onChange={updateWeather}
className="p-3 rounded-lg bg-slate-800 border border-white/10 focus:ring-2 focus:ring-yellow-400 outline-none"/>

<input name="wind" placeholder="Wind km/h" value={manualWeather.wind} onChange={updateWeather}
className="p-3 rounded-lg bg-slate-800 border border-white/10 focus:ring-2 focus:ring-yellow-400 outline-none"/>

</div>

</div>

{/* EXAMPLES */}

<div className="flex flex-wrap gap-4">

<button onClick={()=>setExample({
fire_count:2, avg_frp:3, max_frp:5, night_ratio:0.1, confidence:0.9, trend:-1
})}
className="bg-green-600 hover:bg-green-700 px-5 py-2 rounded-lg font-semibold transition">
Low Example
</button>

<button onClick={()=>setExample({
fire_count:45, avg_frp:20, max_frp:40, night_ratio:0.5, confidence:0.7, trend:1
})}
className="bg-yellow-500 hover:bg-yellow-600 px-5 py-2 rounded-lg font-semibold transition">
Medium Example
</button>

<button onClick={()=>setExample({
fire_count:120, avg_frp:50, max_frp:100, night_ratio:0.9, confidence:0.95, trend:1
})}
className="bg-red-600 hover:bg-red-700 px-5 py-2 rounded-lg font-semibold transition">
High Example
</button>

</div>

{/* FORM */}

<form onSubmit={runPrediction}
className="bg-slate-900/80 backdrop-blur-md p-5 rounded-xl shadow-xl border border-white/10 grid md:grid-cols-2 gap-4">

<input name="fire_count" value={form.fire_count} onChange={update} placeholder="Fire Count"
className="p-3 rounded-lg bg-slate-800 border border-white/10"/>

<input name="avg_frp" value={form.avg_frp} onChange={update} placeholder="Avg FRP"
className="p-3 rounded-lg bg-slate-800 border border-white/10"/>

<input name="max_frp" value={form.max_frp} onChange={update} placeholder="Max FRP"
className="p-3 rounded-lg bg-slate-800 border border-white/10"/>

<input name="night_ratio" value={form.night_ratio} onChange={update} placeholder="Night Fire Ratio"
className="p-3 rounded-lg bg-slate-800 border border-white/10"/>

<input name="confidence" value={form.confidence} onChange={update} placeholder="Confidence Score"
className="p-3 rounded-lg bg-slate-800 border border-white/10"/>

<input name="trend" value={form.trend} onChange={update} placeholder="Fire Trend"
className="p-3 rounded-lg bg-slate-800 border border-white/10"/>

<button className="col-span-2 bg-yellow-400 hover:bg-yellow-300 text-black font-bold p-3 rounded-lg transition">
🔥 Run AI Prediction
</button>

</form>

</div>

);
}