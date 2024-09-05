import React from "react";
import { useSelector, useDispatch } from "react-redux";
import {
   Grid,
   Typography,
   makeStyles,
   Button,
   alpha,
   Chip,
   Box,
   Avatar,
   Container,
} from "@material-ui/core";
import classNames from "classnames";
import { addToCart } from "../../Redux/cartSlice";
import { openSnackBar } from "../../Redux/appSlice";

import ItemList from "../ItemList/ItemList";
import DrawBox from "../DrawBox/DrawBox";
import Upload from "../DropImageBox/DropImageBox";

import CarouselBox from "../CarouselBox/CarouselBox";

const useStyles = makeStyles((theme) => ({
   container: {
      display: "flex",
      padding: theme.spacing(4),
      justifyContent: "space-around",
      // height: "auto",
      height: "100%",
      alignItems: "center",
      [theme.breakpoints.up("md")]: {
         padding: theme.spacing(10),
      },
   },
   imgContainer: {
      width: "300px",
      height: "400px",
      // width: "100%",
      // height: "100%",
      // height: "400px",
      
      boxShadow: theme.shadows[3],
      p: 2, border: '1px solid grey',
   },
   img: {
      width: "300px",
      height: "400px",
      // width: "100%",
      // height:"100%",
      objectFit: "contain"
      // height: "auto",
   },
   marginTopTwo: {
      marginTop: theme.spacing(2),
   },
   paleText: {
      color: alpha("#333", 0.8),
   },
   letterSpace: {
      letterSpacing: 2.5,
   },
}));

const SingleProduct = () => {
   const { singleItem } = useSelector((state) => state.app);
   const { pending, error } = useSelector((state) => state.cart);
   const user = useSelector((state) => state.user.user);
    
   const [selectedImage, setSelectedImage] = React.useState(null);
   function handlesetSelectedImageState(filePath) { setSelectedImage(filePath);}

   const classes = useStyles();
   // TODO 
   const { title, price, description, category, colors, _id  } = singleItem;

   const [color, setColor] = React.useState(Object.keys(colors)[0])
   const [ size, setSize ] = React.useState("")

   const [ sizeDict, setSizeDict ] = React.useState({ S: colors[color]["s_no"], 
                                                      M: colors[color]["m_no"],
                                                      L: colors[color]["l_no"],
                                                      XL: colors[color]["xl_no"],
                                                      XXL: colors[color]["xxl_no"] })

   const [ imageList, setImageList ] = React.useState(colors[color]["image_list"])

   const handleColorClick = (event, key) => {
      setImageList(colors[key]["image_list"])
      setColor(key)

      setSizeDict({ S: colors[key]["s_no"], 
                    M: colors[key]["m_no"],
                    L: colors[key]["l_no"],
                    XL: colors[key]["xl_no"],
                    XXL: colors[key]["xxl_no"] 
                  })
   } 
   const handleSizeClick = () => {
      setSize()
   }

   const dispatch = useDispatch();

   const handleClick = () => {
      if (!user) {
         dispatch(openSnackBar({ severity: "error", text: "Please Log In" }));
      } else {
         dispatch(addToCart(_id));
         if (!error && !pending) {
            dispatch(
               openSnackBar({
                  severity: "success",
                  text: "Item has been added to cart",
               })
            );
         } else if (error && !pending) {
            dispatch(
               openSnackBar({
                  severity: "error",
                  text: "Something went wrong",
               })
            );
         }
      }
   };

   return (
      <>
      <Grid container className={classes.container}>
         <Grid item xs={12} sm={3}>
            <div className={classes.imgContainer}>
               <CarouselBox imageList={imageList}/>
            </div>
         </Grid>
         <Grid item xs={12} sm={3}>
            <div className={classes.imgContainer}>
               {selectedImage ? (
                  <Box     
                     width={300}
                     height={400}
                     sx={{
                     backgroundImage: `url(${URL.createObjectURL(selectedImage)})`,
                     backgroundSize: 'contain',
                     backgroundRepeat: 'no-repeat',
                     backgroundPosition: 'center',
                     // Other styles
                     }}
                   >
                     <DrawBox /> 
                   </ Box>  

                  ) : (
                     <Upload change = {handlesetSelectedImageState}/>
               )}
            </div>
         </Grid> 

         <Grid item xs={12} sm={3}>
            <Grid container> 
               <Grid xs={12}>
                  <Typography className={classes.marginTopTwo} variant="h4">{title}</Typography>
               </Grid>
               <Grid xs={12}>
                  <Chip label={category} variant="outlined" className={classes.marginTopTwo}/>
               </Grid>
               <Grid xs={12}>
                  <Typography className={classNames(classes.paleText, classes.marginTopTwo)} variant="body1">
                     {description}
                  </Typography>
               </Grid>
               <Grid xs={12}>
                  <Typography className={classes.marginTopTwo} variant="subtitle2">
                     ${price}
                  </Typography>
               </Grid>
               {/* --------COLOR---------- */}
               <Grid xs={12}>
                  <Typography className={classNames(classes.paleText, classes.marginTopTwo)} variant="body1" >
                     COLOR: {color}
                  </Typography>
               </Grid>
               <Grid>
                  {Object.keys(colors).map((key) => (
                     <Grid key={key} item>
                        <Avatar alt="img.." src={colors[key]["img_dir"]} onClick={(event) => handleColorClick(event, key)} variant="rounded" />
                     </Grid>
                  )) }
               </Grid>
               {/* SIZE */}
               <Grid container justifyContent="center" spacing={2}>
                  <Typography className={classNames(classes.paleText, classes.marginTopTwo)} variant="body1" >
                     SIZE: {size}
                  </Typography>
               </Grid> 
               <Grid container justifyContent="center" spacing={2}>
               </Grid>
               {/* ADD to card button */}
               <Grid item xs={12}>
                  <Button
                     className={classNames(classes.letterSpace, classes.marginTopTwo)}
                     fullWidth
                     variant="contained"
                     color="primary"
                     disabled={pending}
                     onClick={handleClick}
                  >
                     Add to Cart
                  </Button> 

               </Grid>

            </Grid>
         </Grid>  

      </Grid>
      <ItemList />

      </>
   );
};

export default SingleProduct;
