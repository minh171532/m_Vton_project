import { Card, CardMedia } from '@material-ui/core';
import React, {useState, useEffect} from 'react'
import Carousel from "react-carousel-mui";

import { createTheme, responsiveFontSizes } from '@material-ui/core'; 
// TODO  
const AppTheme = (mode) => createTheme({});
const theme = responsiveFontSizes(AppTheme("light"));

const CustomCard = ({ url }) => {
    return (
        <img src={url} alt="hehe" style={{width:200, height:300, objectFit: "contain" }}   />

        // <Card sx={{ Width: 280, height:380 }}>
        //     <CardMedia component="img" image={url}/>
        // </Card>
    );
};

const CarouselBox = ({imageList}) => {
    const [carouselIndex, setCarouselIndex] = useState(0)

    const handleSlideChange = (index) => {
        // Update the current slide index of both Carousels
        setCarouselIndex(index);
    };
      
    return (
        <>
            <Carousel                 
                items={imageList}
                itemsPerPage={{
                  xs: 1,
                  sm: 1,
                  tablet: 1,
                  md: 1,
                  lg: 1,
                  xl: 1
                }}
                itemRenderer={(item) => <CustomCard url={item} />}
                maxContainerWidth={theme.breakpoints.values["md"]}

                carouselId="myCarousel" 
                onChange={handleSlideChange} 
                currentSlide={carouselIndex}
            />
        </>

    ) 
}


export default CarouselBox;