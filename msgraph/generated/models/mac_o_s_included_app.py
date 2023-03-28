from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class MacOSIncludedApp(AdditionalDataHolder, Parsable):
    """
    Contains properties of an included .app in a MacOS app.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new macOSIncludedApp and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The CFBundleIdentifier.
        self._bundle_id: Optional[str] = None
        # The CFBundleVersion.
        self._bundle_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The CFBundleIdentifier.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The CFBundleIdentifier.
        Args:
            value: Value to set for the bundle_id property.
        """
        self._bundle_id = value
    
    @property
    def bundle_version(self,) -> Optional[str]:
        """
        Gets the bundleVersion property value. The CFBundleVersion.
        Returns: Optional[str]
        """
        return self._bundle_version
    
    @bundle_version.setter
    def bundle_version(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleVersion property value. The CFBundleVersion.
        Args:
            value: Value to set for the bundle_version property.
        """
        self._bundle_version = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSIncludedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSIncludedApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSIncludedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "bundleVersion": lambda n : setattr(self, 'bundle_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_str_value("bundleVersion", self.bundle_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

