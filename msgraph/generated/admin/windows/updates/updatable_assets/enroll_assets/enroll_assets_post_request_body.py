from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

updatable_asset = lazy_import('msgraph.generated.models.windows_updates.updatable_asset')
update_category = lazy_import('msgraph.generated.models.windows_updates.update_category')

class EnrollAssetsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the enrollAssets method.
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
    def assets(self,) -> Optional[List[updatable_asset.UpdatableAsset]]:
        """
        Gets the assets property value. The assets property
        Returns: Optional[List[updatable_asset.UpdatableAsset]]
        """
        return self._assets
    
    @assets.setter
    def assets(self,value: Optional[List[updatable_asset.UpdatableAsset]] = None) -> None:
        """
        Sets the assets property value. The assets property
        Args:
            value: Value to set for the assets property.
        """
        self._assets = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new enrollAssetsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assets property
        self._assets: Optional[List[updatable_asset.UpdatableAsset]] = None
        # The updateCategory property
        self._update_category: Optional[update_category.UpdateCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EnrollAssetsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EnrollAssetsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EnrollAssetsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assets": lambda n : setattr(self, 'assets', n.get_collection_of_object_values(updatable_asset.UpdatableAsset)),
            "update_category": lambda n : setattr(self, 'update_category', n.get_enum_value(update_category.UpdateCategory)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("assets", self.assets)
        writer.write_enum_value("updateCategory", self.update_category)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def update_category(self,) -> Optional[update_category.UpdateCategory]:
        """
        Gets the updateCategory property value. The updateCategory property
        Returns: Optional[update_category.UpdateCategory]
        """
        return self._update_category
    
    @update_category.setter
    def update_category(self,value: Optional[update_category.UpdateCategory] = None) -> None:
        """
        Sets the updateCategory property value. The updateCategory property
        Args:
            value: Value to set for the updateCategory property.
        """
        self._update_category = value
    

