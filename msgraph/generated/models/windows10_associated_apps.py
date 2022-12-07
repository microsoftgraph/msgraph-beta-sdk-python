from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows10_app_type = lazy_import('msgraph.generated.models.windows10_app_type')

class Windows10AssociatedApps(AdditionalDataHolder, Parsable):
    """
    Windows 10 Associated Application definition.
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
    
    @property
    def app_type(self,) -> Optional[windows10_app_type.Windows10AppType]:
        """
        Gets the appType property value. Windows 10 Application type.
        Returns: Optional[windows10_app_type.Windows10AppType]
        """
        return self._app_type
    
    @app_type.setter
    def app_type(self,value: Optional[windows10_app_type.Windows10AppType] = None) -> None:
        """
        Sets the appType property value. Windows 10 Application type.
        Args:
            value: Value to set for the appType property.
        """
        self._app_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windows10AssociatedApps and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Windows 10 Application type.
        self._app_type: Optional[windows10_app_type.Windows10AppType] = None
        # Identifier.
        self._identifier: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10AssociatedApps:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10AssociatedApps
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10AssociatedApps()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_type": lambda n : setattr(self, 'app_type', n.get_enum_value(windows10_app_type.Windows10AppType)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def identifier(self,) -> Optional[str]:
        """
        Gets the identifier property value. Identifier.
        Returns: Optional[str]
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identifier property value. Identifier.
        Args:
            value: Value to set for the identifier property.
        """
        self._identifier = value
    
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
        writer.write_enum_value("appType", self.app_type)
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

