from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Settings(AdditionalDataHolder, Parsable):
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
        Instantiates a new settings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies if the user's primary mailbox is hosted in the cloud and is enabled for Microsoft Graph.
        self._has_graph_mailbox: Optional[bool] = None
        # Specifies if the user has a MyAnalytics license assigned.
        self._has_license: Optional[bool] = None
        # Specifies if the user opted out of MyAnalytics.
        self._has_opted_out: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Settings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Settings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Settings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "has_graph_mailbox": lambda n : setattr(self, 'has_graph_mailbox', n.get_bool_value()),
            "has_license": lambda n : setattr(self, 'has_license', n.get_bool_value()),
            "has_opted_out": lambda n : setattr(self, 'has_opted_out', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def has_graph_mailbox(self,) -> Optional[bool]:
        """
        Gets the hasGraphMailbox property value. Specifies if the user's primary mailbox is hosted in the cloud and is enabled for Microsoft Graph.
        Returns: Optional[bool]
        """
        return self._has_graph_mailbox
    
    @has_graph_mailbox.setter
    def has_graph_mailbox(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasGraphMailbox property value. Specifies if the user's primary mailbox is hosted in the cloud and is enabled for Microsoft Graph.
        Args:
            value: Value to set for the hasGraphMailbox property.
        """
        self._has_graph_mailbox = value
    
    @property
    def has_license(self,) -> Optional[bool]:
        """
        Gets the hasLicense property value. Specifies if the user has a MyAnalytics license assigned.
        Returns: Optional[bool]
        """
        return self._has_license
    
    @has_license.setter
    def has_license(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasLicense property value. Specifies if the user has a MyAnalytics license assigned.
        Args:
            value: Value to set for the hasLicense property.
        """
        self._has_license = value
    
    @property
    def has_opted_out(self,) -> Optional[bool]:
        """
        Gets the hasOptedOut property value. Specifies if the user opted out of MyAnalytics.
        Returns: Optional[bool]
        """
        return self._has_opted_out
    
    @has_opted_out.setter
    def has_opted_out(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasOptedOut property value. Specifies if the user opted out of MyAnalytics.
        Args:
            value: Value to set for the hasOptedOut property.
        """
        self._has_opted_out = value
    
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
        writer.write_bool_value("hasGraphMailbox", self.has_graph_mailbox)
        writer.write_bool_value("hasLicense", self.has_license)
        writer.write_bool_value("hasOptedOut", self.has_opted_out)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

