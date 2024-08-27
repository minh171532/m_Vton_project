import React, { useState } from "react";
import { Container, Button } from "@mui/material";
import { useDropzone } from "react-dropzone";
import UploadIcon from "@mui/icons-material/Upload";
import styles from "./app/containers/Inference/css/InferenceLayout.module.scss";
import ImageNotSupportedIcon from "@mui/icons-material/ImageNotSupported";
import axios_client from "./axiosClient";

const NoImage = () => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
        padding: "20px",
        width: "450px",
        height: "300px",
        // border: '2px solid #ccc',
        // background: '#f7f4f4',
        // borderRadius: '8px'
      }}
    >
      <ImageNotSupportedIcon style={{ fontSize: 50 }} />
      <p
        style={{
          marginTop: "10px",
          fontSize: "16px",
        }}
      >
        No Image Available
      </p>
    </div>
  );
};

const TestUpload = () => {
  const [fileList, setfileList] = useState([]);
  const [resultList, setresultList] = useState([]);

  const onDrop = (acceptedFiles) => {
    console.log(acceptedFiles);
    acceptedFiles.forEach((file) => {
      setfileList((prestate) => [
        {
          imgPath: URL.createObjectURL(file),
          fileName: file.path,
          file_content: file,
        },
        ...prestate,
      ]);
      setresultList((prevstate) => [
        {
          filename: file.path,
          clusterId: "",
          location: "",
          formType: "",
          accountNumber: "",
        },
        ...prevstate,
      ]);
    });
  };

  const handleOnclick = () => {
    if (fileList.length === 0) {
      console.log("no file selected");
      return;
    }
    const fd = new FormData();
    for (let i = 0; i < fileList.length; i++) {
      fd.append("files", fileList[i].file_content);
    }

    fd.append("user_id", "117d3b36-bc30-403e-9abb-126d133bd51c");
    fd.append("clustering_job_id", "1");
    // console.log(fd);
    axios_client
      .post(`api/inference_job/upload`, fd, {
        headers: { "Content-Type": "multipart/form-data" },
      })
      .then((res) => {
        // console.log(res);
        // console.log(res.data["result"]);
        let ret = JSON.parse(res.data["result"].replace(/'/g, '"'));
        // console.log("ret: ", ret);
        let temp = [];
        Object.entries(ret).forEach(([key, result]) => {
          temp.push({
            filename: key,
            clusterId: result.cluster,
            location: result.LOCAL_GOV_NAME,
            formType: result.KIND_OF_TAX,
            accountNumber: result.ACNT_NUM,
          });
        });
        console.log("temp: ", temp);
        setresultList(temp);
      })
      .catch((err) => console.log(err));
  };

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  const [selectedImage, setSelectedImage] = useState("");
  const [resultIndex, setResultIndex] = useState(-1);
  const handleFileClick = (filePath, selectedFileName) => {
    setSelectedImage(filePath);

    let index = resultList.findIndex((element) => {
      return element.filename == selectedFileName;
    });
    console.log("index: ", index);
    setResultIndex(index);
  };

  const inferenceData = {
    filename: "",
    clusterId: "",
    location: "",
    formType: "",
    accountNumber: "",
  };

  return (
    <>
      <Container
        style={{
          display: "flex",
          alignItems: "center",
          gap: "10px",
          justifyContent: "center",
        }}
      >
        {/* FileDrop */}
        <div
          {...getRootProps()}
          style={{
            width: "250px",
            height: "200px",
            backgroundColor: "#f7f4f4",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            border: "2px dashed gray",
            borderRadius: "4px",
            marginTop: "20px",
            position: "relative",
          }}
        >
          <input {...getInputProps()} style={{ display: "none" }} />

          <div style={{ textAlign: "center" }}>
            <UploadIcon style={{ fontSize: "48px", color: "gray" }} />
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

        <Button
          variant="contained"
          onClick={() => {
            handleOnclick();
          }}
        >
          Apply
        </Button>
      </Container>
      {/* <FileName /> */}
      <>
        <div className={styles.content}>
          {/* Select list file */}
          <div className={styles.fileList}>
            <span>File name</span>
            <select multiple>
              {fileList.map((file) => (
                <option
                  onClick={() => handleFileClick(file.imgPath, file.fileName)}
                >
                  {file.fileName}
                </option>
              ))}
            </select>
          </div>
          <div></div>
          <div className={styles.filePreview}>
            {/* preview image */}
            {selectedImage ? (
              <img
                src={selectedImage}
                style={{ maxWidth: "400px", maxHeight: "400px" }}
                alt="Preview"
              />
            ) : (
              <NoImage />
            )}

            {/* Table result */}
            {resultIndex >= 0 ? (
              <div className={styles.inferenceResult}>
                <p>
                  <strong>Inference Result</strong>
                </p>
                <p>Filename: {resultList[resultIndex].filename}</p>
                <p>Cluster ID: {resultList[resultIndex].clusterId}</p>
                <p>Location: {resultList[resultIndex].location}</p>
                <p>Form Type: {resultList[resultIndex].formType}</p>
                <p>Account Number: {resultList[resultIndex].accountNumber}</p>
              </div>
            ) : (
              <div className={styles.inferenceResult}>
                <p>
                  <strong>Inference Result</strong>
                </p>
                <p>Filename: {inferenceData.filename}</p>
                <p>Cluster ID: {inferenceData.clusterId}</p>
                <p>Location: {inferenceData.location}</p>
                <p>Form Type: {inferenceData.formType}</p>
                <p>Account Number: {inferenceData.accountNumber}</p>
              </div>
            )}
          </div>
        </div>
      </>
    </>
  );
};

export default TestUpload;
