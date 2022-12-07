from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

network_type = lazy_import('msgraph.generated.models.network_type')

class NetworkLocationDetail(AdditionalDataHolder, Parsable):
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
        Instantiates a new networkLocationDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Provides the name of the network used when signing in.
        self._network_names: Optional[List[str]] = None
        # Provides the type of network used when signing in. Possible values are: intranet, extranet, namedNetwork, trusted, unknownFutureValue.
        self._network_type: Optional[network_type.NetworkType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkLocationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NetworkLocationDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NetworkLocationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "network_names": lambda n : setattr(self, 'network_names', n.get_collection_of_primitive_values(str)),
            "network_type": lambda n : setattr(self, 'network_type', n.get_enum_value(network_type.NetworkType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def network_names(self,) -> Optional[List[str]]:
        """
        Gets the networkNames property value. Provides the name of the network used when signing in.
        Returns: Optional[List[str]]
        """
        return self._network_names
    
    @network_names.setter
    def network_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the networkNames property value. Provides the name of the network used when signing in.
        Args:
            value: Value to set for the networkNames property.
        """
        self._network_names = value
    
    @property
    def network_type(self,) -> Optional[network_type.NetworkType]:
        """
        Gets the networkType property value. Provides the type of network used when signing in. Possible values are: intranet, extranet, namedNetwork, trusted, unknownFutureValue.
        Returns: Optional[network_type.NetworkType]
        """
        return self._network_type
    
    @network_type.setter
    def network_type(self,value: Optional[network_type.NetworkType] = None) -> None:
        """
        Sets the networkType property value. Provides the type of network used when signing in. Possible values are: intranet, extranet, namedNetwork, trusted, unknownFutureValue.
        Args:
            value: Value to set for the networkType property.
        """
        self._network_type = value
    
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
        writer.write_collection_of_primitive_values("networkNames", self.network_names)
        writer.write_enum_value("networkType", self.network_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

