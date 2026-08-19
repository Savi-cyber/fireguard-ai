import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from "react-leaflet";
import { useState } from "react";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Fix leaflet marker icon issue
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png",
  iconUrl:
    "https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png",
  shadowUrl:
    "https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png",
});

function ClickMarker({ setLocation }) {
  const [position, setPosition] = useState(null);

  useMapEvents({
    click(e) {
      const { lat, lng } = e.latlng;

      setPosition([lat, lng]);

      setLocation({
        lat: lat,
        lng: lng,
      });
    },
  });

  return position === null ? null : (
    <Marker position={position}>
      <Popup>
        Selected Location <br />
        Latitude: {position[0].toFixed(4)} <br />
        Longitude: {position[1].toFixed(4)}
      </Popup>
    </Marker>
  );
}

export default function WildfireMap({ setLocation }) {
  return (
    <div style={{ marginTop: "20px" }}>
      <h2 style={{ marginBottom: "10px" }}>Select Location on Map</h2>

      <MapContainer
        center={[20.5937, 78.9629]}
        zoom={5}
        style={{
          height: "400px",
          width: "100%",
          borderRadius: "10px",
        }}
      >
        <TileLayer
          attribution="© OpenStreetMap"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <ClickMarker setLocation={setLocation} />
      </MapContainer>
    </div>
  );
}