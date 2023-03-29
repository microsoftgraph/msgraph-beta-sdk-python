from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_gallery_image_status, entity

from . import entity

class CloudPcGalleryImage(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcGalleryImage and sets the default values.
        """
        super().__init__()
        # The official display name of the gallery image. Read-only.
        self._display_name: Optional[str] = None
        # The date in which this image is no longer within long-term support. The Cloud PC continues to provide short-term support. Read-only.
        self._end_date: Optional[date] = None
        # The date when the image is no longer available. Read-only.
        self._expiration_date: Optional[date] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The offer name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        self._offer: Optional[str] = None
        # The official display offer name of the gallery image. For example, Windows 10 Enterprise + OS Optimizations. Read-only.
        self._offer_display_name: Optional[str] = None
        # The publisher name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        self._publisher: Optional[str] = None
        # Recommended Cloud PC SKU for this gallery image. Read-only.
        self._recommended_sku: Optional[str] = None
        # The size of this image in gigabytes. Read-only.
        self._size_in_g_b: Optional[int] = None
        # The SKU name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        self._sku: Optional[str] = None
        # The official display stock keeping unit (SKU) name of this gallery image. For example, 2004. Read-only.
        self._sku_display_name: Optional[str] = None
        # The date when the image becomes available. Read-only.
        self._start_date: Optional[date] = None
        # The status of the gallery image on the Cloud PC. Possible values are: supported, supportedWithWarning, notSupported, unknownFutureValue. Read-only.
        self._status: Optional[cloud_pc_gallery_image_status.CloudPcGalleryImageStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcGalleryImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcGalleryImage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcGalleryImage()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The official display name of the gallery image. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The official display name of the gallery image. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def end_date(self,) -> Optional[date]:
        """
        Gets the endDate property value. The date in which this image is no longer within long-term support. The Cloud PC continues to provide short-term support. Read-only.
        Returns: Optional[date]
        """
        return self._end_date
    
    @end_date.setter
    def end_date(self,value: Optional[date] = None) -> None:
        """
        Sets the endDate property value. The date in which this image is no longer within long-term support. The Cloud PC continues to provide short-term support. Read-only.
        Args:
            value: Value to set for the end_date property.
        """
        self._end_date = value
    
    @property
    def expiration_date(self,) -> Optional[date]:
        """
        Gets the expirationDate property value. The date when the image is no longer available. Read-only.
        Returns: Optional[date]
        """
        return self._expiration_date
    
    @expiration_date.setter
    def expiration_date(self,value: Optional[date] = None) -> None:
        """
        Sets the expirationDate property value. The date when the image is no longer available. Read-only.
        Args:
            value: Value to set for the expiration_date property.
        """
        self._expiration_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_gallery_image_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "offer": lambda n : setattr(self, 'offer', n.get_str_value()),
            "offerDisplayName": lambda n : setattr(self, 'offer_display_name', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "recommendedSku": lambda n : setattr(self, 'recommended_sku', n.get_str_value()),
            "sizeInGB": lambda n : setattr(self, 'size_in_g_b', n.get_int_value()),
            "sku": lambda n : setattr(self, 'sku', n.get_str_value()),
            "skuDisplayName": lambda n : setattr(self, 'sku_display_name', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_gallery_image_status.CloudPcGalleryImageStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def offer(self,) -> Optional[str]:
        """
        Gets the offer property value. The offer name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        Returns: Optional[str]
        """
        return self._offer
    
    @offer.setter
    def offer(self,value: Optional[str] = None) -> None:
        """
        Sets the offer property value. The offer name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        Args:
            value: Value to set for the offer property.
        """
        self._offer = value
    
    @property
    def offer_display_name(self,) -> Optional[str]:
        """
        Gets the offerDisplayName property value. The official display offer name of the gallery image. For example, Windows 10 Enterprise + OS Optimizations. Read-only.
        Returns: Optional[str]
        """
        return self._offer_display_name
    
    @offer_display_name.setter
    def offer_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the offerDisplayName property value. The official display offer name of the gallery image. For example, Windows 10 Enterprise + OS Optimizations. Read-only.
        Args:
            value: Value to set for the offer_display_name property.
        """
        self._offer_display_name = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The publisher name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The publisher name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    @property
    def recommended_sku(self,) -> Optional[str]:
        """
        Gets the recommendedSku property value. Recommended Cloud PC SKU for this gallery image. Read-only.
        Returns: Optional[str]
        """
        return self._recommended_sku
    
    @recommended_sku.setter
    def recommended_sku(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedSku property value. Recommended Cloud PC SKU for this gallery image. Read-only.
        Args:
            value: Value to set for the recommended_sku property.
        """
        self._recommended_sku = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_str_value("offer", self.offer)
        writer.write_str_value("offerDisplayName", self.offer_display_name)
        writer.write_str_value("publisher", self.publisher)
        writer.write_str_value("recommendedSku", self.recommended_sku)
        writer.write_int_value("sizeInGB", self.size_in_g_b)
        writer.write_str_value("sku", self.sku)
        writer.write_str_value("skuDisplayName", self.sku_display_name)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
    
    @property
    def size_in_g_b(self,) -> Optional[int]:
        """
        Gets the sizeInGB property value. The size of this image in gigabytes. Read-only.
        Returns: Optional[int]
        """
        return self._size_in_g_b
    
    @size_in_g_b.setter
    def size_in_g_b(self,value: Optional[int] = None) -> None:
        """
        Sets the sizeInGB property value. The size of this image in gigabytes. Read-only.
        Args:
            value: Value to set for the size_in_g_b property.
        """
        self._size_in_g_b = value
    
    @property
    def sku(self,) -> Optional[str]:
        """
        Gets the sku property value. The SKU name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        Returns: Optional[str]
        """
        return self._sku
    
    @sku.setter
    def sku(self,value: Optional[str] = None) -> None:
        """
        Sets the sku property value. The SKU name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
        Args:
            value: Value to set for the sku property.
        """
        self._sku = value
    
    @property
    def sku_display_name(self,) -> Optional[str]:
        """
        Gets the skuDisplayName property value. The official display stock keeping unit (SKU) name of this gallery image. For example, 2004. Read-only.
        Returns: Optional[str]
        """
        return self._sku_display_name
    
    @sku_display_name.setter
    def sku_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the skuDisplayName property value. The official display stock keeping unit (SKU) name of this gallery image. For example, 2004. Read-only.
        Args:
            value: Value to set for the sku_display_name property.
        """
        self._sku_display_name = value
    
    @property
    def start_date(self,) -> Optional[date]:
        """
        Gets the startDate property value. The date when the image becomes available. Read-only.
        Returns: Optional[date]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[date] = None) -> None:
        """
        Sets the startDate property value. The date when the image becomes available. Read-only.
        Args:
            value: Value to set for the start_date property.
        """
        self._start_date = value
    
    @property
    def status(self,) -> Optional[cloud_pc_gallery_image_status.CloudPcGalleryImageStatus]:
        """
        Gets the status property value. The status of the gallery image on the Cloud PC. Possible values are: supported, supportedWithWarning, notSupported, unknownFutureValue. Read-only.
        Returns: Optional[cloud_pc_gallery_image_status.CloudPcGalleryImageStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_gallery_image_status.CloudPcGalleryImageStatus] = None) -> None:
        """
        Sets the status property value. The status of the gallery image on the Cloud PC. Possible values are: supported, supportedWithWarning, notSupported, unknownFutureValue. Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

