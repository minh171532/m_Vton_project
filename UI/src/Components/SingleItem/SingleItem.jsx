import React from "react";
import {
   makeStyles,
   Card,
   CardMedia,
   Grid,
   Typography,
   CardActionArea,
   CardContent,
   Avatar,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
   root: {
      maxWidth: 500,
      [theme.breakpoints.up("sm")]: {
         maxHeight: 400,
      },
   },
   media: {
      height: 140,
      [theme.breakpoints.up("sm")]: {
         height: 200,
      },
   },
}));

const SingleItem = ({ item }) => {
   const classes = useStyles();
   const { _id, title, colors, price } = item;
   const images = Object.values(colors);

   const navigate = useNavigate();
   return (
      <Grid item xs={10} sm={6} lg={3}>
         <Card className={classes.root}>
            <CardActionArea onClick={() => navigate(`/products/${_id}`)}>
               <CardMedia
                  className={classes.media}
                  src={images[0]}
                  title={title}
                  component="img"
                  loading="lazy"
               />
               <CardContent>
                  <Typography gutterBottom variant="body1" component="h4">
                     {title.substring(0, 20)}...
                  </Typography>
                  <Typography
                     variant="body2"
                     color="textSecondary"
                     component="p"
                  >
                     ${price}
                  </Typography>
               </CardContent>

               <Grid container justifyContent="center" spacing={2}>
                  {images.map((image_, index) => (
                     <Grid key={index} item>
                        <Avatar alt="img.." src={image_} variant="square" />
                     </Grid>
                  ))}
               </Grid>

            </CardActionArea>
         </Card>
      </Grid>
   );
};

export default SingleItem;
