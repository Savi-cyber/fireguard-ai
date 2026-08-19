import { MapContainer, TileLayer, Marker, useMapEvents } from "react-leaflet";
import { useState } from "react";
import "leaflet/dist/leaflet.css";

function ClickMarker({ setLocation }) {

  const [pos,setPos] = useState(null);

  useMapEvents({
    click(e){

      let {lat,lng} = e.latlng;

      // FIX LONGITUDE RANGE
      if(lng > 180){
        lng = lng - 360;
      }

      if(lng < -180){
        lng = lng + 360;
      }

      const weather = {
        lat,
        lng,
        temperature: Math.floor(25 + Math.random()*10),
        humidity: Math.floor(30 + Math.random()*40),
        wind: Math.floor(5 + Math.random()*10)
      };

      setLocation(weather);
      setPos([lat,lng]);
    }
  });

  return pos ? <Marker position={pos}/> : null;
}

export default function MapSelector({ setLocation }) {

  return (

    <div style={{height:"350px"}}>

      <MapContainer center={[20.5937,78.9629]} zoom={5} style={{height:"100%"}}>

        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>

        <ClickMarker setLocation={setLocation}/>

      </MapContainer>

    </div>

  );
}