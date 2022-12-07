from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AndroidManagedStoreAppTrack(AdditionalDataHolder, Parsable):
    """
    Contains track information for Android Managed Store apps.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new androidManagedStoreAppTrack and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Friendly name for track.
        self._track_alias: Optional[str] = None
        # Unique track identifier.
        self._track_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAppTrack:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppTrack
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreAppTrack()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "track_alias": lambda n : setattr(self, 'track_alias', n.get_str_value()),
            "track_id": lambda n : setattr(self, 'track_id', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("trackAlias", self.track_alias)
        writer.write_str_value("trackId", self.track_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def track_alias(self,) -> Optional[str]:
        """
        Gets the trackAlias property value. Friendly name for track.
        Returns: Optional[str]
        """
        return self._track_alias
    
    @track_alias.setter
    def track_alias(self,value: Optional[str] = None) -> None:
        """
        Sets the trackAlias property value. Friendly name for track.
        Args:
            value: Value to set for the trackAlias property.
        """
        self._track_alias = value
    
    @property
    def track_id(self,) -> Optional[str]:
        """
        Gets the trackId property value. Unique track identifier.
        Returns: Optional[str]
        """
        return self._track_id
    
    @track_id.setter
    def track_id(self,value: Optional[str] = None) -> None:
        """
        Sets the trackId property value. Unique track identifier.
        Args:
            value: Value to set for the trackId property.
        """
        self._track_id = value
    

