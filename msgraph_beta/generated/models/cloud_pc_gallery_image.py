from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcGalleryImage(Entity):
    # The official display name of the gallery image. Read-only.
    display_name: Optional[str] = None
    # The date in which this image is no longer within long-term support. The Cloud PC continues to provide short-term support. Read-only.
    end_date: Optional[datetime.date] = None
    # The date when the image is no longer available. Read-only.
    expiration_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offer name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
    offer: Optional[str] = None
    # The official display offer name of the gallery image. For example, Windows 10 Enterprise + OS Optimizations. Read-only.
    offer_display_name: Optional[str] = None
    # The publisher name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
    publisher: Optional[str] = None
    # Recommended Cloud PC SKU for this gallery image. Read-only.
    recommended_sku: Optional[str] = None
    # The size of this image in gigabytes. Read-only.
    size_in_g_b: Optional[int] = None
    # The SKU name of the gallery image. This value is passed to Azure to get the image resource. Read-only.
    sku: Optional[str] = None
    # The official display stock keeping unit (SKU) name of this gallery image. For example, 2004. Read-only.
    sku_display_name: Optional[str] = None
    # The date when the image becomes available. Read-only.
    start_date: Optional[datetime.date] = None
    # The status of the gallery image on the Cloud PC. Possible values are: supported, supportedWithWarning, notSupported, unknownFutureValue. Read-only.
    status: Optional[CloudPcGalleryImageStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcGalleryImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcGalleryImage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcGalleryImage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
        from .entity import Entity

        from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
        from .entity import Entity

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
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcGalleryImageStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
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
    

