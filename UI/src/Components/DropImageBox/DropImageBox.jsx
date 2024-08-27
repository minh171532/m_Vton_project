import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import PublishIcon from '@material-ui/icons/Publish';

const Upload = ({ change }) => {

    const onDrop = (acceptedFiles) => {
      change(acceptedFiles[0])
        // setfileList((prestate) => [
        //   {
        //     imgPath: URL.createObjectURL(acceptedFiles[0]),
        //     fileName: acceptedFiles[0].path,
        //     file_content: acceptedFiles[0],
        //   },
        //   ...prestate,
        // ]);

      };


    const { getRootProps, getInputProps } = useDropzone({ onDrop });
    return (
        <div
          {...getRootProps()}
          style={{
            width: "300px",
            height: "400px",
            backgroundColor: "#f7f4f4",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            border: "2px dashed gray",
            borderRadius: "4px",
            // marginTop: "20px",
            position: "relative",
          }}
        >
          <input {...getInputProps()} style={{ display: "none" }} />
          <div style={{ textAlign: "center" }}>
            <PublishIcon style={{ fontSize: "48px", color: "gray" }} />
            <div>
              <b style={{ textAlign: "center", margin: "5px" }}>
                Drag file(s) here to upload
              </b>
              <p style={{ textAlign: "center", color: "gray", margin: "5px" }}>
                Alternatively, you can select a file by
              </p>
              <b style={{ textAlign: "center", color: "blue", margin: "5px" }}>
                clicking here
              </b>
            </div>
          </div>
        </div>
    )

}

export default Upload




