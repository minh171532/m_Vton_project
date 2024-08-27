import React from 'react';
import { Stage, Layer, Line, Text } from 'react-konva';

// function from https://stackoverflow.com/a/15832662/512042
function downloadURI(uri, name) {
    var link = document.createElement('a');
    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }


const DrawBox = () => {
  const [tool, setTool] = React.useState('pen');
  const [lines, setLines] = React.useState([]);
  const isDrawing = React.useRef(false);
  const stageRef = React.useRef(null);

  React.useEffect(() => {
    const stage = stageRef.current;

    const preventDefault = (e) => {
      e.preventDefault();
    };
    // Add event listeners to prevent scrolling
    stage.content.addEventListener('touchstart', preventDefault, { passive: false });
    stage.content.addEventListener('touchmove', preventDefault, { passive: false });
    stage.content.addEventListener('touchend', preventDefault, { passive: false });
    return () => {
      // Clean up event listeners
      stage.content.removeEventListener('touchstart', preventDefault);
      stage.content.removeEventListener('touchmove', preventDefault);
      stage.content.removeEventListener('touchend', preventDefault);
    };
    }, []);
  const handleExport = () => {
    const uri = stageRef.current.toDataURL();
    // const blob = new Blob([uri], { type: 'image/png' }); // file : URL.createObjectURL(blob);
    // console.log(URL.createObjectURL(blob));

    downloadURI(uri, 'stage.png');
  };

  const handleTouchstart = (e) => {
    // e.preventDefault();
    isDrawing.current = true;
    const pos = e.target.getStage().getPointerPosition();
    setLines([...lines, { tool, points: [pos.x, pos.y] }]);
  }
  const handleTouchmove = (e) => {
      if (!isDrawing.current) {
        return;
      }
      const stage = e.target.getStage();
      const point = stage.getPointerPosition();
      let lastLine = lines[lines.length - 1];
      // add point
      lastLine.points = lastLine.points.concat([point.x, point.y]);
  
      // replace last
      lines.splice(lines.length - 1, 1, lastLine);
      setLines(lines.concat());
  }
  const handleTouchend = (e) => {
    isDrawing.current = false;
  }
  const handleMouseDown = (e) => {
    isDrawing.current = true;
    const pos = e.target.getStage().getPointerPosition();
    setLines([...lines, { tool, points: [pos.x, pos.y] }]);
  };
  const handleMouseMove = (e) => {
    // no drawing - skipping
    if (!isDrawing.current) {
      return;
    }
    const stage = e.target.getStage();
    const point = stage.getPointerPosition();
    let lastLine = lines[lines.length - 1];
    // add point
    lastLine.points = lastLine.points.concat([point.x, point.y]);

    // replace last
    lines.splice(lines.length - 1, 1, lastLine);
    setLines(lines.concat());
  };
  const handleMouseUp = () => {
    isDrawing.current = false;
  };

  return (
    <div>
      <button onClick={handleExport}>Click here to log stage data URL</button>
      <Stage
        // width={window.innerWidth}
        // height={window.innerHeight}
        width={"300"}
        height={"400"}
        onMouseDown={handleMouseDown}
        onMousemove={handleMouseMove}
        onMouseup={handleMouseUp}
        onTouchstart={handleTouchstart}
        onTouchmove={handleTouchmove}
        onTouchend={handleTouchend}
        ref={stageRef}
      >
        <Layer>
          {/* <Text text="Just start drawing" x={5} y={30} /> */}
          {lines.map((line, i) => (
            <Line
              key={i}
              points={line.points}
              stroke="#df4b26"
              strokeWidth={line.tool === 'eraser' ? 25 : 20}
              tension={0.5}
              lineCap="round"
              lineJoin="round"
              globalCompositeOperation={
                line.tool === 'eraser' ? 'destination-out' : 'source-over'
              }
            />
          ))}
        </Layer>
      </Stage>
      <select
        value={tool}
        onChange={(e) => {
          setTool(e.target.value);
        }}
      >
        <option value="pen">Pen</option>
        <option value="eraser">Eraser</option>
      </select>
    </div>
  );
};

export default DrawBox;